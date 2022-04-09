<template>
  <div>
    <router-link to="/search"> <button>Back to search</button></router-link>

    <div class="container">
      <h1>Stock Price Chart ({{ this.$route.params.code }})</h1>
      <div ref="chart" class="chart" width="960" height="512" />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import * as d3 from "d3";

const margin = { top: 30, right: 80, bottom: 30, left: 80 };
const width = 960 - margin.left - margin.right;
const height = 512 - margin.top - margin.bottom;

export default {
  name: "SearchView",
  data() {
    return {
      stock: null,
    };
  },

  created() {
    // watch the params of the route to fetch the data again
    this.token = localStorage.getItem("hkspc-token");

    this.$watch(
      () => this.$route.params,
      () => {
        this.fetchData();
      },

      // fetch the data when the view is created and the data is
      // already being observed
      { immediate: true }
    );
  },
  watch: {
    stock(newVal) {
      const data = newVal.map((item) => {
        return {
          date: d3.timeParse("%Y-%m-%d")(item.fields.time),
          value: item.fields.closed_price,
          volume: item.fields.volume,
        };
      });

      const bisectDate = d3.bisector(function (d) {
        return d.date;
      }).left;

      // Add tooltip to the chart
      const pointermoved = (e) => {
        const x0 = x.invert(d3.pointer(e)[0] - margin.left);
        const i = bisectDate(data, x0, 1);

        const d0 = data[i - 1];
        const d1 = data[i];
        const d = x0 - d0?.date > d1?.date - x0 ? d1 : d0;
        focus.style("display", "block");
        focus
          .select("circle")
          .attr(
            "transform",
            "translate(" + x(d?.date) + "," + y(d?.value) + ")"
          );
        focus
          .select(".closed_price")
          .attr("x", x(d?.date) - 48)
          .attr("y", y(d?.value) + 20)
          .text("Closed Price: " + d?.value)
          .style("font-size", 14);

        focus
          .select(".volume")
          .attr("x", x(d?.date) - 48)
          .attr("y", y(d?.value) + 40)
          .text("Volume: " + d?.volume)
          .style("font-size", 14);

        focus
          .select(".date")
          .attr("x", x(d?.date) - 48)
          .attr("y", y(d?.value) - 12)
          .text(
            "Date: " +
              new Date(Date.parse(d?.date)).toLocaleDateString("en-US", {
                month: "short",
                day: "numeric",
              })
          )
          .style("font-size", 14);
      };

      // Remove tooltip
      const pointerleft = (d) => {
        focus.style("display", "none");
      };

      // Add whole svg to the DOM
      const svg = d3
        .select(this.$refs.chart)
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .on("pointerenter pointermove", pointermoved)
        .on("pointerleave", pointerleft)
        .on("touchstart", (event) => event.preventDefault())
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

      const focus = svg.append("g").style("display", "none");

      // Add tooltip

      // Add X axis
      const x = d3
        .scaleTime()
        .domain(
          d3.extent(data, function (d) {
            return d.date;
          })
        )
        .range([0, width]);
      svg
        .append("g")
        .attr("transform", `translate(0, ${height})`)
        .call(d3.axisBottom(x));

      // Add Y axis
      const y = d3
        .scaleLinear()
        .domain([
          0,
          d3.max(data, function (d) {
            return +d.value;
          }),
        ])
        .range([height, 0]);
      svg.append("g").call(d3.axisLeft(y));

      // Add the line
      svg
        .append("path")
        .datum(data)
        .attr("fill", "none")
        .attr("stroke", "#2c3e50")
        .attr("stroke-width", 1.5)
        .attr(
          "d",
          d3
            .line()
            .defined(function (d) {
              return d.value !== null;
            })
            .x(function (d) {
              return x(d.date);
            })
            .y(function (d) {
              return y(d.value);
            })
        );

      focus
        .append("circle")
        .attr("fill", "#42b983")
        .attr("stroke", "#42b983")
        .attr("r", 4);
      focus.append("text").classed("closed_price", true);
      focus.append("text").classed("volume", true);
      focus.append("text").classed("date", true);
    },
  },
  methods: {
    fetchData() {
      if (this.$route.params.code)
        axios
          .get("http://localhost:8000/stocks/getstock", {
            params: { code: this.$route.params.code, token: this.token },
          })
          .then((response) => {
            this.stock = response.data;
          })
          .catch((error) => {
            console.log(error);
            if (error.response.status === 500) {
              alert("Your session has expired. Please login again.");
              this.$router.push("/");
            }
          });
    },
  },
};
</script>

<style scoped>
button {
  border: none;
  border-radius: 3px;
  padding: 0.5rem;
  font-size: 1rem;
  outline: none;
  cursor: pointer;
  background-color: #42b983;
  margin-left: 16px;
}

h1 {
  text-align: center;
}

.chart {
  width: 960px;
  height: 512px;
}

.container {
  display: flex;
  flex-direction: column;
  justify-content: center;

  width: 960px;
  margin: 16px auto;
  padding: 1rem;
  gap: 2rem;
}
</style>

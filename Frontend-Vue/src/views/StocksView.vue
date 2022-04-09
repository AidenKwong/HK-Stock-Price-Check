<template>
  <div>
    <form class="form" @submit.prevent="handleSubmit">
      <h1>Stock</h1>
      <div class="queryBox">
        <input
          v-model="stockCode"
          type="text"
          placeholder="stock code"
          required
        />
        <button>Search</button>
      </div>
    </form>

    <ul id="example-1">
      <li v-for="itm in stock" :key="itm.fields.pk">
        {{ JSON.stringify(itm.fields) }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "StocksView",
  data() {
    return {
      stockCode: "",
      stock: "",
    };
  },
  methods: {
    handleSubmit() {
      axios
        .get("http://localhost:8000/stocks/getstock", {
          params: { code: this.stockCode },
        })
        .then((response) => {
          this.stock = response.data;
        });
    },
  },
};
</script>

<style scoped>
.form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin: 0 auto;
  width: 324px;
}

.queryBox {
  display: flex;
  flex-direction: row;
  gap: 1rem;
}

input {
  border: 1px solid #2c3e50;
  border-radius: 3px;
  padding: 0.5rem;
  font-size: 1rem;
  outline: none;
}

button {
  border: none;
  border-radius: 3px;
  padding: 0.5rem;
  font-size: 1rem;
  flex: 1;
  outline: none;
  cursor: pointer;
  background-color: #42b983;
}
</style>

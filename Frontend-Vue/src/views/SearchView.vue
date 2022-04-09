<template>
  <div>
    <form class="form" @submit.prevent="handleSubmit">
      <h1>Stock</h1>
      <div>
        Available stocks:
        <span v-for="item in availableCodes" :key="item">{{ item }}, </span>
      </div>
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
  </div>
</template>

<script>
export default {
  name: "SearchView",
  data() {
    return {
      stockCode: "",
      availableCodes: ["5", "700", "939", "941", "9988"],
    };
  },
  methods: {
    handleSubmit() {
      if (this.availableCodes.includes(this.stockCode)) {
        this.$router.push(`/stocks/${this.stockCode}`);
      } else {
        alert("Invalid stock code");
      }
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

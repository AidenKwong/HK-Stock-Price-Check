<template>
  <div>
    <nav>
      <div class="navContent">
        <router-link to="/" class="home">
          <h2>HK Stock Price Check</h2></router-link
        >
        <button @click="logout" class="logout"><h3>logout</h3></button>
      </div>
    </nav>
    <router-view />
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      user: null,
    };
  },
  created() {
    this.user = localStorage.getItem("user");
  },
  methods: {
    logout() {
      localStorage.removeItem("hkspc-token");
      alert("logout successfully");
      this.$router.push("/");
    },
  },
};
</script>

<style>
* {
  margin: 0;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

nav {
  background-color: #42b983;
}

.navContent {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 2.5rem;
  max-width: 1320px;
  margin: 0 auto 1rem auto;
  padding: 0 1rem;
}

.home {
  text-decoration: none;
  color: #2c3e50;
}

.logout {
  color: #2c3e50;
  border: none;
  border-radius: 2px;
  height: 1.5rem;
  cursor: pointer;
}
</style>

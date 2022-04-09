<template>
  <form class="form" @submit.prevent="handleSubmit">
    <h2>Login</h2>
    <input
      v-model="username_email"
      type="text"
      placeholder="Username / Email Address"
      required
    />
    <input v-model="password" type="password" placeholder="Password" required />
    <button class="button">Login</button>
    <router-link to="/signup" class="link">Create account</router-link>
  </form>
</template>

<script>
import axios from "axios";

export default {
  name: "Login",
  data() {
    return {
      username_email: "",
      password: "",
    };
  },
  methods: {
    handleSubmit() {
      axios
        .get("http://127.0.0.1:8000/users/login", {
          params: {
            "username/email": this.username_email,
            password: this.password,
          },
        })
        .then((res) => {
          if (res.status === 200) {
            alert("Login successful");
            localStorage.setItem("hkspc-token", res.data);
            this.$router.push("/search");
          }
        })
        .catch((err) => {
          console.log(err);
          if (err.response.status === 401) {
            alert("Wrong email or password");
          }
        });
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.form {
  width: 256px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
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
  outline: none;
  cursor: pointer;
  background-color: #42b983;
}

.link {
  text-align: start;
  color: #2c3e50;
}
</style>

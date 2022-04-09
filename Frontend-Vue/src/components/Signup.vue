<template>
  <form class="form" @submit.prevent="handleSubmit">
    <h2>Sign Up</h2>
    <input v-model="username" type="text" placeholder="Username" required />
    <input v-model="email" type="text" placeholder="Email Address" required />
    <input v-model="password" type="password" placeholder="Password" required />
    <input
      v-model="confirmPassword"
      type="password"
      placeholder="Confirm Password"
      required
    />
    <button class="button">Sign Up</button>
    <router-link to="/" class="link">Login</router-link>
  </form>
</template>

<script>
import axios from "axios";

export default {
  name: "Signup",
  data() {
    return {
      username: "",
      email: "",
      password: "",
      confirmPassword: "",
    };
  },
  methods: {
    handleSubmit() {
      if (this.password !== this.confirmPassword) {
        alert("Passwords do not match");
        return;
      } else {
        axios
          .post("http://127.0.0.1:8000/users/signup", {
            username: this.username,
            email: this.email,
            password: this.password,
          })
          .then((res) => {
            if (res.status === 201) {
              alert("Signup successful");
              this.$router.push("/");
            }
          })
          .catch((err) => {
            console.log(err);
            if (err.response.status === 409) {
              alert("Email already exists");
            }
          });
      }
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

<template>
  <div>
    <Signup />
  </div>
</template>

<script>
// @ is an alias to /src
import Signup from "@/components/Signup.vue";

export default {
  name: "LoginView",
  components: {
    Signup,
  },
};
</script>

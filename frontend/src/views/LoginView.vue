<template>
  <form @submit.prevent="submit">
    <h1 class="h3 mb-3 fw-normal">Please sign in</h1>
    <input v-model="data.email" type="email" class="form-control" placeholder="name@example.com">
    <input v-model="data.password" type="password" class="form-control" placeholder="password">
    <button class="w-100 btn btn-lg btn-primary" type="submit">Sign in</button>
  </form>
</template>

<script lang="ts">
import {reactive} from 'vue';
import {useRouter} from "vue-router";

export default {
  name: "LoginView",
  setup() {
    const data = reactive({
      email: '',
      password: ''
    });

    const router = useRouter();

    const submit = async () => {
      console.log(data);
      const response = await fetch(process.env.VUE_APP_ROOT_API + '/users/login', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        credentials: 'include',
        body: JSON.stringify(data)
      });
      const content = await response.json();
      console.log('>>> J W T <<<');
      console.log(content.jwt);
      await router.push('/');
    }

    return {
      data,
      submit
    }
  }
}
</script>

<style scoped>

</style>
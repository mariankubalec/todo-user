<template>
  <form @submit.prevent="submit" class="form-signin w-100 m-auto">
    <h1 class="h3 mb-3 fw-normal">Please register</h1>
    <input v-model="data.name" class="form-control" placeholder="Name">
    <input v-model="data.email" type="email" class="form-control" placeholder="name@example.com">
    <input v-model="data.password" type="password" class="form-control" placeholder="Password">
    <button class="w-100 btn btn-lg btn-primary" type="submit">Register</button>
  </form>
</template>

<script lang="ts">
import {reactive} from 'vue';
import {useRouter} from "vue-router";

export default {
  name: "RegisterView",
  setup() {
    const data = reactive({
      name: '',
      email: '',
      password: ''
    });
    const router = useRouter();

    const submit = async () => {
      console.log('>>> R E G I S T E R <<<');
      console.log(data);
      console.log(process.env.VUE_APP_ROOT_API);
      await fetch(process.env.VUE_APP_ROOT_API + '/users/register', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
      });

      await router.push('/login');
    }

    return {
      data,
      submit
    }
  }
}
</script>
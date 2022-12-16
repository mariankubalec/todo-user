<template>
  <form @submit.prevent="submit" class="form-signin w-100 m-auto">
    <h1 class="h3 mb-3 fw-normal">Please sign in</h1>
    <input v-model="data.email" type="email" class="form-control" placeholder="name@example.com">
    <input v-model="data.password" type="password" class="form-control" placeholder="password">
    <button class="w-100 btn btn-lg btn-primary" type="submit">Sign in</button>
  </form>
</template>

<script lang="ts">
import {reactive} from 'vue';
import {useRouter} from "vue-router";
import {useStore} from "vuex";


export default {
  name: "LoginView",
  setup() {
    const store = useStore();

    const data = reactive({
      email: '',
      password: ''
    });

    const router = useRouter();

    const submit = async () => {
      try {
        const response = await fetch(process.env.VUE_APP_ROOT_API + '/users/login', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          credentials: 'include',
          body: JSON.stringify(data)
        });
        const content = await response.json();
        if (content.jwt) {
          localStorage.setItem('jwt', content.jwt);
          localStorage.setItem('user-name', content.name);
          await store.dispatch('setAuth', true);
        }
      } catch (e) {
        console.log(e)
      }

      router.push('/');
    }

    return {
      data,
      submit
    }
  }
}
</script>

<style scoped>
/*.form-signin {*/
/*  max-width: 330px;*/
/*  padding: 15px;*/
/*}*/

/*.form-signin .form-floating:focus-within {*/
/*  z-index: 2;*/
/*}*/

/*.form-signin input[type="email"] {*/
/*  margin-bottom: -1px;*/
/*  border-bottom-right-radius: 0;*/
/*  border-bottom-left-radius: 0;*/
/*}*/

/*.form-signin input[type="password"] {*/
/*  margin-bottom: 10px;*/
/*  border-top-left-radius: 0;*/
/*  border-top-right-radius: 0;*/
/*}*/
</style>
<template>
  <div class="home-view">
    <div v-if="auth">
      <form @submit.prevent="submit" class="form-signin w-100 m-auto">
        <h1 class="h3 mb-3 fw-normal">Add Todo</h1>
        <label for="title">Title:</label>
        <input v-model="data.title" type="text" id="username" class="form-control" placeholder="Title" required>
        <label for="description">Description:</label>
        <input v-model="data.description" type="text" id="description" class="form-control"
               placeholder="Description">
        <label for="is_urgent">Is urgent:<span class="tab1"></span></label>
        <input v-model="data.is_urgent" type="checkbox" id="is_urgent"><br>
        <label for="is_done">Is done:<span class="tab1"></span></label>
        <input v-model="data.is_done" type="checkbox" id="is_done"><br>
        <label for="due_date">Due date:</label>
        <input v-model="data.due_date" type="datetime-local" id="due_date" class="form-control">
        <button class="w-100 btn btn-lg btn-primary" type="submit">Add</button>
      </form>
    </div>
    <div v-else>"You are not logged in!"</div>
  </div>
</template>

<script lang="ts">
import {reactive, computed} from 'vue';
import {useRouter} from "vue-router";
import {useStore} from "vuex";

export default {
  name: "AddTodoView",

  setup() {
    const data = reactive({
      title: '',
      description: '',
      is_urgent: '',
      is_done: '',
      due_date: '',
    });

    const router = useRouter();
    const store = useStore();
    const auth = computed(() => store.state.authenticated);

    const submit = async () => {
      try {
        const value = localStorage.getItem("jwt") || "";
        console.log(JSON.stringify(data));
        await fetch(process.env.VUE_APP_ROOT_API + '/todos/add', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': value
          },
          credentials: 'include',
          body: JSON.stringify(data)
        });
      } catch (e) {
        console.log(e)
        await store.dispatch('setAuth', false);
      }

      router.push('/');
    }

    return {
      data,
      submit,
      auth,
    }
  }
}
</script>

<style scoped>
.tab1 {
  display: inline-block;
  margin-left: 20px;
}
.home-view {
  width: 100%;
  padding: 20px;
}
</style>

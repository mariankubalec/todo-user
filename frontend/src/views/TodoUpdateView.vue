<template>
  <div class="home-view">
    <div v-if="auth">
      <div v-if="todo">
        <form @submit.prevent="submit" class="form-signin w-100 m-auto">
          <h1 class="h3 mb-3 fw-normal">Update Todo</h1>
          <label for="title">Title:</label>
          <input v-model="data.title" type="text" id="username" class="form-control" required>
          <label for="description">Description:</label>
          <input v-model="data.description" type="text" id="description" class="form-control">
          <label for="is_urgent">Is urgent:<span class="tab1"></span></label>
          <input v-model="data.is_urgent" type="checkbox" id="is_urgent"><br>
          <label for="is_done">Is done:<span class="tab1"></span></label>
          <input v-model="data.is_done" type="checkbox" id="is_done"><br>
          <label for="due_date">Due date:</label>
          <input v-model="data.due_date" type="datetime-local" id="due_date" class="form-control">
          <button class="w-100 btn btn-lg btn-primary" type="submit">Update</button>
        </form>
      </div>
    </div>
    <div v-else>"You are not logged in!"</div>
  </div>
</template>

<script lang="ts">
import { onMounted, reactive, computed, ref} from 'vue';
import { useRouter, useRoute } from "vue-router";
import { useStore } from "vuex";

export default {
  name: "TodoUpdateView",

  setup() {
    const data = reactive({
      title: '',
      description: '',
      is_urgent: Boolean,
      is_done: Boolean,
      due_date: '',
    });

    const router = useRouter();
    const route = useRoute();
    const store = useStore();
    const auth = computed(() => store.state.authenticated);
    let todo = ref();

    onMounted(async () => {
      try {
        const value = localStorage.getItem("jwt") || "";
        console.log(route.params);
        const response = await fetch(process.env.VUE_APP_ROOT_API + '/todos/' + route.params.id, {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': value
          },
          credentials: 'include',
        });

        todo.value = await response.json();

        data.title = todo.value.title;
        data.description = todo.value.description;
        data.is_urgent = todo.value.is_urgent;
        data.is_done = todo.value.is_done;
        let date:string = todo.value.due_date;
        console.log(date);
        date = date.substring(0, date.length - 1);
        console.log(date);
        data.due_date = date;

        console.log(todo.value);
        console.log(data);

      } catch (e) {
        console.log(e)
        await store.dispatch('setAuth', false);
      }
    });

    const submit = async () => {
      try {
        const value = localStorage.getItem("jwt") || "";
        console.log(JSON.stringify(data));
        await fetch(process.env.VUE_APP_ROOT_API + '/todos/' + route.params.id,  {
          method: 'PUT',
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
      todo,
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

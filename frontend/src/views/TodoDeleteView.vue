<template>
  <div class="home-view">
    <div class="form-signin w-100 m-auto" v-if="auth">
      <div v-if="todo">
        <h1 class="h3 mb-3 fw-normal">Delete Todo id:{{ $route.params.id }}</h1>
        <h3 class="h5 mb-3 fw-normal">Title: <b>{{ todo.title }}</b></h3>
        <h3 class="h5 mb-3 fw-normal">Description:</h3>
        <p>{{ todo.description }}</p>
        <h3 class="h5 mb-3 fw-normal">
          Is urgent:
          <span v-if="todo.is_urgent" >
            YES
          </span>
          <span v-else>
            NO
          </span>
        </h3>
        <h3 class="h5 mb-3 fw-normal">
          Is done: 
          <span v-if="todo.is_done" >
            YES
          </span>
          <span v-else>
            NO
          </span>
        </h3>
        <h3 class="h5 mb-3 fw-normal">
          Creation date: 
          <span v-text="getFormattedDateTime(todo.creation_date)"></span>
        </h3>
        <h3 class="h5 mb-3 fw-normal">
          Due date:
          <span v-text="getFormattedDateTime(todo.due_date)"></span>
        </h3>
        <button class="w-100 btn btn-lg btn-primary red-background" @click="deleteTodo()">Delete</button>
      </div>
      <div v-else>
        Hmm...
      </div>
    </div>
    <div v-else>"You are not logged in!"</div>
  </div>
</template>

<script lang="ts">
import { onMounted, computed, ref } from 'vue';
import { useRoute, useRouter } from "vue-router";
import { useStore } from "vuex";
import { getFormattedDateTime } from "../services/todo-view-service";

export default {
  name: "TodoDeleteView",
  components: {
  },

  methods: {
    getFormattedDateTime(input: string): string {
      return getFormattedDateTime(input);
    },
  },

  setup() {
    const route = useRoute();
    const router = useRouter();
    const store = useStore();
    const auth = computed(() => store.state.authenticated);
    let todo = ref();

    const deleteTodo = async (): Promise<void> => {
      try {
        const value = localStorage.getItem("jwt") || "";
        await fetch(process.env.VUE_APP_ROOT_API + '/todos/' + route.params.id, {
          method: 'DELETE',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': value
          },
          credentials: 'include',
        });
      } catch (e) {
        console.log(e)
        await store.dispatch('setAuth', false);
      }

      router.push('/');
    };

    onMounted(async () => {
      try {
        const value = localStorage.getItem("jwt") || "";
        const response = await fetch(process.env.VUE_APP_ROOT_API + '/todos/' + route.params.id, {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': value
          },
          credentials: 'include',
        });

        todo.value = await response.json();
      } catch (e) {
        console.log(e)
        await store.dispatch('setAuth', false);
      }
    });

    return {
      auth,
      todo,
      deleteTodo,
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
.red-background {
  background: red;
  border-color: red;
}
</style>

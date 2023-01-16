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
import { useRoute } from "vue-router";
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

        console.log(todo.value);

      } catch (e) {
        console.log(e)
        await store.dispatch('setAuth', false);
      }
    });

    return {
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

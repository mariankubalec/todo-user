<template>
  <div class="home-view">
    {{ message }}
    <div v-if="auth">
      <div>Your todos:</div>
      <!-- <router-link to="/add-todo">Add todo</router-link> -->
      <router-link :to="{ name: 'add' }">Add todo</router-link>
      <div v-if="todo?.length > 0">
        <table class="styled-table">
          <thead>
            <tr>
              <th>Title</th>
              <th>Urgent</th>
              <th>Done</th>
              <th>Created</th>
              <th>Due</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in todo" :key=item.id>
              <td><router-link :to="{ name: 'TodoViewSingle', params: {id: item.id} }">{{ item.title }}</router-link></td>
              <td>{{ item.is_urgent }}</td>
              <td>{{ item.is_done }}</td>
              <td v-text="getFormattedDateTime(item.creation_date)"></td>
              <td v-text="getFormattedDateTime(item.due_date)"></td>
              <td>
                <router-link :to="{ name: 'TodoEditSingle', params: {id: item.id} }">Edit</router-link>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div v-else>You have no Todos.</div>
    </div>
  </div>
</template>

<script lang="ts">
import {onMounted, ref, computed} from "vue";
import {useStore} from "vuex";
import { getFormattedDateTime } from "../services/todo-view-service";

export default {
  name: "HomeView",

  methods: {
    getFormattedDateTime(input: string): string {
      return getFormattedDateTime(input);
    },
  },
  // methods: {
  //   getFormattedDateTime(input: string): string {
  //     if (input) {
  //       return input.substring(0, input.indexOf('T'));
  //     } else {
  //       return '';
  //     }
  //   },
  // },

  setup() {
    const message = ref("You are not logged in!");
    const store = useStore();
    const todos = ref([]);

    const auth = computed(() => store.state.authenticated);
    onMounted(async () => {
      try {
        const value = localStorage.getItem("jwt") || "";
        let name;

        let response = await fetch(process.env.VUE_APP_ROOT_API + '/users/user', {
          headers: {
            'Content-Type': 'application/json',
            'Authorization': value
          },
          credentials: 'include'
        });

        let content = await response.json();

        if (content.name) {
          name = content.name;
          message.value = `Hi ${name}`;
          await store.dispatch('setAuth', true);
        }
        response = await fetch(process.env.VUE_APP_ROOT_API + '/todos/list', {
          headers: {
            'Content-Type': 'application/json',
            'Authorization': value
          },
          credentials: 'include'
        });
        todos.value = await response.json();

      } catch (e) {
        await store.dispatch('setAuth', false);
      }
    });

    return {
      message,
      todo: todos,
      auth,
    }
  },
}
</script>

<style scoped>
.home-view {
  width: 100%;
  padding: 20px;
}

.styled-table {
  border-collapse: collapse;
  margin: 25px 0;
  font-size: 0.9em;
  font-family: sans-serif;
  min-width: 400px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
}

.styled-table thead tr {
  background-color: #009879;
  color: #ffffff;
  text-align: left;
}

.styled-table th,
.styled-table td {
  padding: 12px 15px;
}

.styled-table tbody tr {
  border-bottom: 1px solid #dddddd;
}

.styled-table tbody tr:nth-of-type(even) {
  background-color: #f3f3f3;
}

.styled-table tbody tr:last-of-type {
  border-bottom: 2px solid #009879;
}

.styled-table tbody tr.active-row {
  font-weight: bold;
  color: #009879;
}

</style>

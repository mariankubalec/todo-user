<template>
  <nav class="navbar navbar-expand-md navbar-dark bg-dark mb-4">
    <div class="container-fluid" v-if="!auth">
      <router-link to="/" class="navbar-brand">Home</router-link>
      <div class="navbar-brand">TODOappV0</div>
      
      <div>
        <ul class="navbar-nav me-auto mb-2 mb-md-0">
          <li class="nav-item">
            <router-link to="/login" class="nav-link">Login</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/register" class="nav-link">Register</router-link>
          </li>
        </ul>
      </div>
    </div>
    <div class="container-fluid" v-if="auth">
      <router-link to="/" class="navbar-brand" v-text="getHomeText()"></router-link>
      <div class="navbar-brand">TODOappV0</div>
      <div>
        <ul class="navbar-nav me-auto mb-2 mb-md-0" v-if="auth">
          <li class="nav-item">
            <router-link to="/login" class="nav-link" @click="logout">Logout</router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script lang="ts">
import {computed} from "vue";
import {useStore} from "vuex";

export default {
  name: "NavBar",

  methods: {
    getHomeText(): string {
      let toReturn = 'Home';
      let name = localStorage.getItem("user-name");
      if (name != null) {
        toReturn = toReturn + ' for the ' + name.toUpperCase()
      }
      return toReturn;
    }
  },

  setup() {
    const store = useStore();
    // const homeText = ref("Home");

    const auth = computed(() => store.state.authenticated);

    const logout = async () => {
      localStorage.removeItem('jwt')
      localStorage.removeItem('user-name')
      window.location.reload();
    }
    // console.log(auth.value);
    // console.log(localStorage.getItem("user-name"))
    // if (auth.value && localStorage.getItem("user-name") != null) {
    //   homeText.value = 'Home for ' + localStorage.getItem("user-name");
    // }

    return {
      auth,
      logout,
      // homeText,
    }
  }
}
</script>
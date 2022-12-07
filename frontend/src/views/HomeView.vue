<template>
  {{ message }}
</template>

<script lang="ts">
import {onMounted, ref} from "vue";
import {useStore} from "vuex";

export default {
  name: "HomeView",

  setup() {
    const message = ref("You are not logged in!");
    const store = useStore();

    onMounted(async () => {
      try {
        const response = await fetch(process.env.VUE_APP_ROOT_API + '/users/user', {
          headers: {'Content-Type': 'application/json'},
          credentials: 'include'
        });

        const content = await response.json();

        if (content.name) {
          message.value = `Hi ${content.name}`;
          await store.dispatch('setAuth', true);
        }

      } catch (e) {
        await store.dispatch('setAuth', false);
      }
    });

    return {
      message
    }
  }
}
</script>

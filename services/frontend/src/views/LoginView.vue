<template>
    <section class="max-w-md mx-auto mt-8">
      <form @submit.prevent="submit" class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
        <div class="mb-4">
          <label for="username" class="block text-gray-700 text-sm font-bold mb-2">Username:</label>
          <input type="text" name="username" v-model="form.username" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
        </div>
        <div class="mb-6">
          <label for="password" class="block text-gray-700 text-sm font-bold mb-2">Password:</label>
          <input type="password" name="password" v-model="form.password" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" />
        </div>
        <div class="flex items-center justify-between">
          <button type="submit" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">Submit</button>
        </div>
      </form>
    </section>
  </template>
  
  <script>
  import { defineComponent } from 'vue';
  import { mapActions } from 'vuex';
  
  export default defineComponent({
    name: 'Login',
    data() {
      return {
        form: {
          username: '',
          password: '',
        },
      };
    },
    methods: {
      ...mapActions(['logIn']),
      async submit() {
        const User = new FormData();
        User.append('username', this.form.username);
        User.append('password', this.form.password);
        try {
          await this.logIn(User);
          this.$router.push('/dashboard');
        } catch (error) {
          console.error("Login failed:", error);
        }
      },
    },
  });
  </script>
  
  <style scoped>
  /* Custom styles for better UX can be added here */
  </style>
  
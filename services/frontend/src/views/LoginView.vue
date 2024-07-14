<template>
    <section class="max-w-md mx-auto mt-8">
      <img src="../assets/logo.png" alt="logo" class="mx-auto" />
      <form @submit.prevent="submit" class="bg-white rounded px-16 pb-8">
        <div class="mb-1">
          <input type="text" name="username" v-model="form.username" placeholder="아이디" class="bg-gray-100 shadow appearance-none border rounded-lg w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
        </div>
        <div class="mb-1">
          <input type="password" name="password" v-model="form.password" placeholder="비밀번호" class="bg-gray-100 shadow appearance-none border rounded-lg w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
        </div>
        <div class="flex items-center justify-center">
          <button type="submit" class="bg-red-500 hover:bg-red-700 text-white font-bold w-full py-2 px-3 rounded-lg focus:outline-none focus:shadow-outline">에브리타임 로그인</button>
        </div>
      </form>
      <div class="flex items-center justify-center">
        <router-link to="/register" class="inline-block align-baseline text-sm text-gray-500 hover:text-gray-800 underline">회원가입</router-link>
      </div>
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
  
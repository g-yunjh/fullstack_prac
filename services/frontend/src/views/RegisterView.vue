<template>
    <section class="max-w-md mx-auto">
      <form @submit.prevent="submit" class="bg-white border rounded px-8 pt-6 pb-8 mb-4">
        <div class="mb-14">
          <h1 class="font-bold text-2xl">에브리타임 회원가입</h1>
          <p class = "text-sm text-gray">에브리타임 계정으로 
            <span class="font-bold">캠퍼스픽, 에브리타임</span> 등
            <br />다양한 대학생 서비스를 모두 이용하실 수 있습니다.</p>
        </div>
        <div class="mb-4">
          <label for="username" class="block text-gray-700 font-bold mb-1">아이디: </label>
          <input type="text" name="username" v-model="user.username" placeholder="아이디를 입력하세요." class=" bg-gray-100 shadow appearance-none border rounded-xl w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
        </div>
        <div class="mb-4">
          <label for="full_name" class="block text-gray-700 font-bold mb-1">이름: </label>
          <input type="text" name="full_name" v-model="user.full_name" placeholder="이름을 입력하세요." class="bg-gray-100 shadow appearance-none border rounded-xl w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
        </div>
        <div class="mb-6">
          <label for="password" class="block text-gray-700 font-bold mb-1">비밀번호: </label>
          <input type="password" name="password" v-model="user.password" placeholder="비밀번호를 입력하세요." class="bg-gray-100 shadow appearance-none border rounded-xl w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
        </div>
        <div class="flex items-center justify-center">
          <button type="submit" class=" w-full bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded-xl focus:outline-none focus:shadow-outline">회원가입</button>
        </div>
      </form>
    </section>
  </template>
  
  <script>
  import { defineComponent } from 'vue';
  import { mapActions } from 'vuex';
  
  export default defineComponent({
    name: 'Register',
    data() {
      return {
        user: {
          username: '',
          full_name: '',
          password: '',
        },
      };
    },
    methods: {
      ...mapActions(['register']),
      async submit() {
        try {
          await this.register(this.user);
          this.$router.push('/dashboard');
        } catch (error) {
          throw 'Username already exists. Please try again.';
        }
      },
    },
  });
  </script>
  
  <style scoped>
  /* Custom styles for better UX can be added here */
  </style>
  
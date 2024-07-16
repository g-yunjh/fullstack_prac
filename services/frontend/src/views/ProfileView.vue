<template>
    <section class="max-w-4xl mx-auto mt-8 border rounded-lg mr-5 ml-5">
      <div class="flex justify-between">
        <h1 class="text-2xl font-bold ml-4 mb-4 mt-4">내 정보</h1>
        <p>
        <button @click="deleteAccount()" class="mr-3 mt-3 bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded-lg focus:outline-none focus:shadow-outline">
            계정 삭제
          </button>
        </p>
      </div>
      <div class="flex">
        <div class="ml-7 mt-3">
          <p><svg xmlns="http://www.w3.org/2000/svg" height="90px" viewBox="0 -960 960 960" width="90px" fill="#5f6368"><path d="M200-246q54-53 125.5-83.5T480-360q83 0 154.5 30.5T760-246v-514H200v514Zm280-194q58 0 99-41t41-99q0-58-41-99t-99-41q-58 0-99 41t-41 99q0 58 41 99t99 41ZM200-120q-33 0-56.5-23.5T120-200v-560q0-33 23.5-56.5T200-840h560q33 0 56.5 23.5T840-760v560q0 33-23.5 56.5T760-120H200Zm69-80h422q-44-39-99.5-59.5T480-280q-56 0-112.5 20.5T269-200Zm211-320q-25 0-42.5-17.5T420-580q0-25 17.5-42.5T480-640q25 0 42.5 17.5T540-580q0 25-17.5 42.5T480-520Zm0 17Z"/></svg></p>
        </div>
        <div class="bg-white rounded px-8 pt-6 pb-8">
          <p class="mb-1 font-bold text-2xl"><span>{{ user.full_name }}</span></p>
          <p class="mb-4 text-gray-500 text-sm"><strong>아이디:</strong> <span>{{ user.username }}</span></p>
        </div>
      </div>
    </section>
  </template>
    
  <script>
  import { defineComponent } from 'vue';
  import { mapGetters, mapActions } from 'vuex';
  
  export default defineComponent({
    name: 'Profile',
    created() {
      this.$store.dispatch('viewMe');
    },
    computed: {
      ...mapGetters({ user: 'stateUser' }),
    },
    methods: {
      ...mapActions(['deleteUser']),
      async deleteAccount() {
        try {
          await this.deleteUser(this.user.id);
          await this.$store.dispatch('logOut');
          this.$router.push('/');
        } catch (error) {
          console.error(error);
        }
      },
    },
  });
  </script>
  
  <style scoped>
  /* Custom styles for better UX can be added here */
  </style>
  
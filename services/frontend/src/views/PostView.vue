<template>
    <div v-if="post" class="max-w-4xl mx-auto mt-8 bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
      <p class="mb-4"><strong>Title:</strong> {{ post.title }}</p>
      <p class="mb-4"><strong>Content:</strong> {{ post.content }}</p>
      <p class="mb-4"><strong>Author:</strong> {{ post.author.username }}</p>
  
      <div v-if="user.id === post.author.id" class="mt-4">
        <p><router-link :to="{ name: 'EditPost', params: { id: post.id } }" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">Edit</router-link></p>
        <p><button @click="removePost" class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">Delete</button></p>
      </div>
    </div>
  </template>
  
  <script>
  import { defineComponent } from 'vue';
  import { mapGetters, mapActions } from 'vuex';
  
  export default defineComponent({
    name: 'Post',
    props: ['id'],
    async created() {
      try {
        await this.viewPost(this.id);
      } catch (error) {
        console.error(error);
        this.$router.push('/dashboard');
      }
    },
    computed: {
      ...mapGetters({ post: 'statePost', user: 'stateUser' }),
    },
    methods: {
      ...mapActions(['viewPost', 'deletePost']),
      async removePost() {
        try {
          await this.deletePost(this.id);
          this.$router.push('/dashboard');
        } catch (error) {
          console.error(error);
        }
      }
    },
  });
  </script>
  
  <style scoped>
  /* Custom styles for better UX can be added here */
  </style>
  
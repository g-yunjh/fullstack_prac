<template>
    <section class="max-w-4xl mx-auto mt-8">
      <h1 class="text-2xl font-bold mb-4">Edit Post</h1>
      <hr class="mb-4"/>
  
      <form @submit.prevent="submit" class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
        <div class="mb-4">
          <label for="title" class="block text-gray-700 text-sm font-bold mb-2">Title:</label>
          <input type="text" name="title" v-model="form.title" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
        </div>
        <div class="mb-4">
          <label for="content" class="block text-gray-700 text-sm font-bold mb-2">Content:</label>
          <textarea
            name="content"
            v-model="form.content"
            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          ></textarea>
        </div>
        <button type="submit" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">Submit</button>
      </form>
    </section>
  </template>
  
  <script>
  import { defineComponent } from 'vue';
  import { mapGetters, mapActions } from 'vuex';
  
  export default defineComponent({
    name: 'EditPost',
    props: ['id'],
    data() {
      return {
        form: {
          title: '',
          content: '',
        },
      };
    },
    created() {
      this.GetPost();
    },
    computed: {
      ...mapGetters({ post: 'statePost' }),
    },
    methods: {
      ...mapActions(['updatePost', 'viewPost']),
      async submit() {
        try {
          let post = {
            id: this.id,
            form: this.form,
          };
          await this.updatePost(post);
          this.$router.push({ name: 'Post', params: { id: this.post.id } });
        } catch (error) {
          console.log(error);
        }
      },
      async GetPost() {
        try {
          await this.viewPost(this.id);
          this.form.title = this.post.title;
          this.form.content = this.post.content;
        } catch (error) {
          console.error(error);
          this.$router.push('/dashboard');
        }
      }
    },
  });
  </script>
  
  <style scoped>
  /* Custom styles for better UX can be added here */
  </style>
  
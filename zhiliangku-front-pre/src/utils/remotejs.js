export default {
    components: {
     'remote-js': {
      render(createElement) {
          console.log(999999)
        return createElement('script', { attrs: { type: 'text/javascript', src: this.src }});
      },
      props: {
        src: { type: String, required: true },
      },
    },
    },
  }
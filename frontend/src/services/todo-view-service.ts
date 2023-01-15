// export async function getTodo(): Promise<Todo> {
// //   try {
// //     const value = localStorage.getItem("jwt") || "";
// //     console.log(route.params);
// //     let response = await fetch(process.env.VUE_APP_ROOT_API + '/todos/' + route.params.id, {
// //       method: 'GET',
// //       headers: {
// //         'Content-Type': 'application/json',
// //         'Authorization': value
// //       },
// //       credentials: 'include',
// //     });

// //     todo = await response.json();

// //     console.log(todo);
// //     // console.log(await response.json());

// //   } catch (e) {
// //     console.log(e)
// //     await store.dispatch('setAuth', false);
// //   }
// }

export function getFormattedDateTime(input: string): string {
  if (input) {
    return input.substring(0, input.indexOf('T'));
  } else {
    return '';
  }
}
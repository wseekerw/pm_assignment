import { useSelector } from 'react-redux';

const AllPostsComponent = () => {

  const posts = useSelector(state => state.posts.posts);
  
  return (
    <div className="container">
      <h2 className="mt-4">All Posts</h2>
      <table className="table table-dark table-striped table-bordered table-hover">
        <thead>
          <tr>
            <th scope="col">ID</th>
            <th scope="col">User ID</th>
            <th scope="col">Title</th>
            <th scope="col">Body</th>
          </tr>
        </thead>
        <tbody>
          {posts.map((post) => (
            <tr key={post.id}>
              <td>{post.id}</td>
              <td>{post.userId}</td>
              <td>{post.title}</td>
              <td>{post.body}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default AllPostsComponent;
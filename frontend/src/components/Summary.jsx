import { useSelector } from 'react-redux';

const SummaryComponent = () => {
  const summary = useSelector(state => state.posts?.summary);

  const top_users = summary?.top_users || [];
  const common_words = summary?.common_words || [];

  if (!summary) {
    return <div className="text-light container mt-3">Loading summary...</div>;
  }

  return (
    <div className="container mt-3 text-light">
      <h3>Summary</h3>

      <h5 className="mt-4">Top Users by Unique Words</h5>
      <table className="table table-dark table-striped table-bordered table-hover">
        <thead>
          <tr>
            <th>User ID</th>
            <th>Username</th>
            <th>Unique Word Count</th>
          </tr>
        </thead>
        <tbody>
          {top_users.length === 0 ? (
            <tr>
              <td colSpan="3" className="text-center">No top users found.</td>
            </tr>
          ) : (
            top_users.map((user) => (
              <tr key={user.userId}>
                <td>{ user.userId }</td>
                <td>{ user.username }</td>
                <td>{ user.unique_word_count }</td>
              </tr>
            ))
          )}
        </tbody>
      </table>

      <h5 className="mt-4">Most Frequent Words Across All Titles</h5>
      <table className="table table-dark table-striped table-bordered table-hover">
        <thead>
          <tr>
            <th>Word</th>
            <th>Count</th>
            <th>Username</th>
          </tr>
        </thead>
        <tbody>
          {common_words.length === 0 ? (
            <tr>
              <td colSpan="2" className="text-center">No common words found.</td>
            </tr>
          ) : (
            common_words.map(({ word, count, topUsername }, index) => (
              <tr key={index}>
                <td>{ word }</td>
                <td>{ count }</td>
                <td>{ topUsername }</td>
              </tr>
            ))
          )}
        </tbody>
      </table>
    </div>
  );
};

export default SummaryComponent;
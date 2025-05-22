import { useEffect } from "react";
import { useDispatch } from 'react-redux';
import { fetchAnomalies, fetchPosts, fetchSummary } from '../api/api'
import { setPosts, setAnomalies, setSummary} from '../state/postsSlice'
import  AllPostsComponent  from './AllPosts'
import  SummaryComponent  from './Summary'
import  AnomaliesComponent  from './Anomalies'


const PostsComponent = () => {

  const dispatch = useDispatch();

  useEffect(() => {
    Promise.all([fetchPosts(), fetchAnomalies(), fetchSummary()])
      .then(([postsRes, anomaliesRes, summaryRes]) => {
        // console.log('Posts:', postsRes);
        // console.log('Anomalies:', anomaliesRes);
        // console.log('Summary:', summaryRes);
        dispatch(setPosts(postsRes));
        dispatch(setAnomalies(anomaliesRes));
        dispatch(setSummary(summaryRes));

      })
      .catch(err => {
        console.error('Error fetching data:', err);
      });
  }, []);
  

  return (
    <>
      <AnomaliesComponent />
      <SummaryComponent />
      <AllPostsComponent />
    </>
  );
};

export default PostsComponent;
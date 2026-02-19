import React, { useState, useEffect } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchWorkouts = async () => {
      try {
        const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;
        console.log('Fetching workouts from:', apiUrl);
        
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log('Workouts data received:', data);
        
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results || data;
        console.log('Processed workouts:', workoutsData);
        
        setWorkouts(workoutsData);
        setLoading(false);
      } catch (err) {
        console.error('Error fetching workouts:', err);
        setError(err.message);
        setLoading(false);
      }
    };

    fetchWorkouts();
  }, []);

  if (loading) return <div className="container mt-5"><p>Loading workouts...</p></div>;
  if (error) return <div className="container mt-5"><p className="text-danger">Error: {error}</p></div>;

  return (
    <div className="container mt-5">
      <div className="card workouts-card mb-4">
        <div className="card-header">
          <h2 className="mb-0">💪 Workouts</h2>
        </div>
      </div>
      <div className="row">
        {workouts.map((workout) => (
          <div key={workout.id} className="col-md-6 mb-4">
            <div className="card workouts-card h-100">
              <div className="card-header">
                <h5 className="mb-0">{workout.name}</h5>
              </div>
              <div className="card-body">
                <p className="card-text">{workout.description}</p>
                <ul className="list-group list-group-flush">
                  <li className="list-group-item">🏋️ Type: <strong>{workout.workout_type}</strong></li>
                  <li className="list-group-item">📊 Difficulty: <span className="badge bg-warning text-dark">{workout.difficulty_level}</span></li>
                  <li className="list-group-item">⏱️ Duration: <strong>{workout.duration} minutes</strong></li>
                  <li className="list-group-item">🔥 Calories: <strong>{workout.estimated_calories}</strong></li>
                </ul>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Workouts;

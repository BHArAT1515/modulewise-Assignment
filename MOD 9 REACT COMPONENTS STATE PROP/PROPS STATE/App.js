import UserCard from "./UserCard";
import Counter from "./Counter";

function App() {
    return (
        <div>
            <UserCard name="Alice" age={25} location="New York" />
            <Counter />
        </div>
    );
}

export default App;

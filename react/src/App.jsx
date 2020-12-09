import React, { Component } from "react";

class App extends Component {

	render() {
		return (
        <div>
            <h3>Hellow to RecatJS</h3>
            {["php","java","paython"].map((tech, i) => (
                <button>
                    {tech}
                </button>
            )
            )}
        </div>
        );
	}
}

export default App;
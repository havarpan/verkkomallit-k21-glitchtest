/* global cytoscape */

const getGraph = async function() {
  const data = await fetch("/", {
    method: "POST"
  });
  const posted_json = JSON.parse(await data.json());
  renderGraph(posted_json);
};
getGraph();

/* the above with jquery:
fetch("/", {
    method: "POST"
  })
    .then(res => res.json())
    .then(response => {
      renderGraph(JSON.parse(response))
    });
*/

const renderGraph = function(data) {
  const cy = cytoscape({
    container: document.getElementById("cy"),
    elements: data,
    style: [
      {
        selector: "node",
        style: {
          label: "data(label)",
          "text-halign": "center",
          "text-valign": "center",
          width: "30px",
          height: "30px",
          color: "blue"
        }
      },
      {
        selector: "edge",
        style: {
          label: "data(weight)",
          width: "2px",
          "text-background-color": "yellow",
          "text-background-opacity": 0.4
        }
      }
    ],
    layout: {
      name: "cose"
    }
  });
};

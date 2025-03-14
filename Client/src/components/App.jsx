import React, { useEffect, useState } from "react";
import Header from "./Header";
import Footer from "./Footer";
import Note from "./Note";
import CreateArea from "./CreateArea";

function App() {
  const [notes, setNotes] = useState([]);
console.log(notes);

  const getKeep = async () => {
    try {
      const res = await fetch("http://127.0.0.1:8000/api/note/");
      const data = await res.json();
      setNotes(data);
    } catch (err) {
      console.error(err.message);
    }
  };
  useEffect(() => {
    getKeep();
  }, []);

  async function deleteNote(id) {
    try {
      `4/`
      const deleteKeep = await fetch(`http://127.0.0.1:8000/api/note_delete/${id}/`, {
        method: "DELETE",
      });
      setNotes(notes.filter((note) => note.id !== id));
      console.log(deleteKeep);
    } catch (err) {
      console.error(err);
    }
  }

  return (
    <div>
      <Header />
      <CreateArea />
      {notes.map((noteItem) => {
        return (
          <Note
          id={noteItem.id}
            key={noteItem.id}
            title={noteItem.title}
            content={noteItem.content}
            onDelete={deleteNote}
          />
        );
      })}
      <Footer />
    </div>
  );
}

export default App;

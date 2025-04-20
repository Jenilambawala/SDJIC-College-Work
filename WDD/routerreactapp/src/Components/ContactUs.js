import React, { useState } from 'react'

export const ContactUs = () => {


    // State to track form data and errors
    const [formData, setFormData] = useState({
      name: "",
      email: "",
      subject: "",
      message: "",
    });
  
    const [errors, setErrors] = useState({});
  
    // Validation function
    const validate = () => {
      const validationErrors = {};
      if (!formData.name.trim()) validationErrors.name = "Name is required.";
      if (!formData.email.trim()) {
        validationErrors.email = "Email is required.";
      } else if (!/\S+@\S+\.\S+/.test(formData.email)) {
        validationErrors.email = "Enter a valid email address.";
      }
      if (!formData.subject.trim()) validationErrors.subject = "Subject is required.";
      if (!formData.message.trim()) validationErrors.message = "Message is required.";
      return validationErrors;
    };
  
    // Handle input change
    const handleChange = (e) => {
      const { name, value } = e.target;
      setFormData((prevData) => ({
        ...prevData,
        [name]: value,
      }));
    };
  
    // Handle form submission
    const handleSubmit = (e) => {
      e.preventDefault(); // Prevent default form submission
      const validationErrors = validate();
      if (Object.keys(validationErrors).length > 0) {
        setErrors(validationErrors); // Set errors if validation fails
      } else {
        setErrors({});
        console.log("Form submitted successfully:", formData);
        // You can add further form submission logic here, such as an API call
      }
    };


  return (
    <React.Fragment>
      <div class="container-fluid bg-light py-5">
        <div class="col-md-6 m-auto text-center">
          <h1 class="h1">Contact Us</h1>
          <p>
            Proident, sunt in culpa qui officia deserunt mollit anim id est
            laborum. Lorem ipsum dolor sit amet.
          </p>
        </div>

        <form className="col-md-9 m-auto" onSubmit={handleSubmit}>
          <div className="row">
            <div className="form-group col-md-6 mb-3">
              <label htmlFor="name">Name</label>
              <input
                type="text"
                className="form-control mt-1"
                id="name"
                name="name"
                placeholder="Name"
                value={formData.name}
                onChange={handleChange}
              />
              {errors.name && <small className="text-danger">{errors.name}</small>}
            </div>
            <div className="form-group col-md-6 mb-3">
              <label htmlFor="email">Email</label>
              <input
                type="email"
                className="form-control mt-1"
                id="email"
                name="email"
                placeholder="Email"
                value={formData.email}
                onChange={handleChange}
              />
              {errors.email && <small className="text-danger">{errors.email}</small>}
            </div>
          </div>
          <div className="mb-3">
            <label htmlFor="subject">Subject</label>
            <input
              type="text"
              className="form-control mt-1"
              id="subject"
              name="subject"
              placeholder="Subject"
              value={formData.subject}
              onChange={handleChange}
            />
            {errors.subject && <small className="text-danger">{errors.subject}</small>}
          </div>
          <div className="mb-3">
            <label htmlFor="message">Message</label>
            <textarea
              className="form-control mt-1"
              id="message"
              name="message"
              placeholder="Message"
              rows="8"
              value={formData.message}
              onChange={handleChange}
            />
            {errors.message && <small className="text-danger">{errors.message}</small>}
          </div>
          <div className="row">
            <div className="col text-end mt-2">
              <button type="submit" className="btn btn-success btn-lg px-3">
                Let’s Talk
              </button>
            </div>
          </div>
        </form>

      </div>
    </React.Fragment>
  );
}
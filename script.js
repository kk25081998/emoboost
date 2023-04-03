const quoteForm = document.querySelector("#quote-form");
const quoteOutput = document.querySelector(".quote");

const displaySliderValue = (sliderId, outputId) => {
  const slider = document.querySelector(sliderId);
  const output = document.querySelector(outputId);

  output.textContent = slider.value;

  slider.addEventListener("input", () => {
    output.textContent = slider.value;
  });
};

const generateQuote = async (criteria) => {
  const response = await fetch("/generate_quote", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ criteria }),
  });

  if (response.ok) {
    const data = await response.json();
    return data.quote;
  } else {
    throw new Error("Failed to generate quote.");
  }
};

quoteForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const criteria = [
    quoteForm.elements.criterion1.value,
    quoteForm.elements.criterion2.value,
    quoteForm.elements.criterion3.value,
    // quoteForm.elements.criterion4.value,
  ];
  console.log(criteria);
  try {
    const quote = await generateQuote(criteria);
    quoteOutput.textContent = quote;
  } catch (error) {
    quoteOutput.textContent = "Error: Could not generate quote.";
  }
});

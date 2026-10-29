package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.0 */
import java.util.List;
import lombok.*;

/**
  An organization-defined parameter (ODP): a value, such as a time period or a frequency, that a requirement statement leaves to the organization, with the guideline SP 800-171A gives for defining it. A few parameters are a selection among choices instead of a value.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Sp800171Parameter  {

  private String odpId;
  private String odpLabel;
  private String odpUsage;
  private String odpGuideline;
  private List<String> odpChoices;
  private String odpSelectionCount;

}
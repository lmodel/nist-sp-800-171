package example;

/* metamodel_version: 1.12.0 */
/* version: 3.0.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  One of the three assessment methods SP 800-171A applies to a requirement, examine, interview or test, with the assessment objects (documents, people, processes or mechanisms) it is applied to.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Sp800171AssessmentMethod  {

  private String requirementMethodKind;
  private List<String> requirementMethodObjects;


}
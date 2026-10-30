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
  A security requirement of SP 800-171: a numbered, named requirement for protecting CUI, with its statement, discussion, references and source controls, the organization-defined parameters its statement leaves open, and the assessment objectives and methods SP 800-171A gives it. A requirement that Revision 3 withdrew keeps its number and says which requirements took its place.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Sp800171Requirement  {

  private String title;
  private String description;
  private String requirementId;
  private String requirementStatus;
  private List<String> incorporatedIntoRequirements;
  private List<String> addressedByRequirements;
  private String requirementStatement;
  private List<Sp800171RequirementItem> requirementItems;
  private String requirementDiscussion;
  private List<Sp800171Parameter> requirementParameters;
  private List<Sp800171AssessmentObjective> requirementObjectives;
  private List<Sp800171AssessmentMethod> requirementMethods;
  private List<Sp800171Reference> requirementReferences;
  private List<String> sourceControls;


}
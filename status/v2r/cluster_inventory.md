# V2R cluster inventory

2026-09-24T09:55:39.999009+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324432703488 available bytes; 81.90% used; 112489589 free inodes.

server1 `/home`: 324432703488 available bytes; 81.90% used; 112489589 free inodes.

server1 `/tmp`: 324432703488 available bytes; 81.90% used; 112489589 free inodes.

server1 `/var/tmp`: 324432703488 available bytes; 81.90% used; 112489589 free inodes.

server1 `/mnt/raid5`: 500719513600 available bytes; 97.70% used; 337701895 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57755725824 available bytes; 96.78% used; 110430749 free inodes.

server2 `/home`: 57755725824 available bytes; 96.78% used; 110430749 free inodes.

server2 `/tmp`: 57755725824 available bytes; 96.78% used; 110430749 free inodes.

server2 `/var/tmp`: 57755725824 available bytes; 96.78% used; 110430749 free inodes.

server2 `/mnt/raid5`: 513825918976 available bytes; 96.45% used; 445176993 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85807702016 available bytes; 95.21% used; 114198989 free inodes.

server3 `/home`: 85807702016 available bytes; 95.21% used; 114198989 free inodes.

server3 `/data`: 165595136000 available bytes; 97.71% used; 225819700 free inodes.

server3 `/tmp`: 85807702016 available bytes; 95.21% used; 114198989 free inodes.

server3 `/var/tmp`: 85807702016 available bytes; 95.21% used; 114198989 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105748238336 available bytes; 94.10% used; 114349034 free inodes.

server4 `/home`: 105748238336 available bytes; 94.10% used; 114349034 free inodes.

server4 `/data`: 154559778816 available bytes; 97.86% used; 225273210 free inodes.

server4 `/tmp`: 105748238336 available bytes; 94.10% used; 114349034 free inodes.

server4 `/var/tmp`: 105748238336 available bytes; 94.10% used; 114349034 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.

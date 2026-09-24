# V2R cluster inventory

2026-09-24T08:45:40.282575+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324388098048 available bytes; 81.90% used; 112490300 free inodes.

server1 `/home`: 324388098048 available bytes; 81.90% used; 112490300 free inodes.

server1 `/tmp`: 324388098048 available bytes; 81.90% used; 112490300 free inodes.

server1 `/var/tmp`: 324388098048 available bytes; 81.90% used; 112490300 free inodes.

server1 `/mnt/raid5`: 504342630400 available bytes; 97.69% used; 337718685 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57798074368 available bytes; 96.78% used; 110430958 free inodes.

server2 `/home`: 57798074368 available bytes; 96.78% used; 110430958 free inodes.

server2 `/tmp`: 57798074368 available bytes; 96.78% used; 110430958 free inodes.

server2 `/var/tmp`: 57798074368 available bytes; 96.78% used; 110430958 free inodes.

server2 `/mnt/raid5`: 515687239680 available bytes; 96.44% used; 445179414 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 85899841536 available bytes; 95.21% used; 114199589 free inodes.

server3 `/home`: 85899841536 available bytes; 95.21% used; 114199589 free inodes.

server3 `/data`: 173622972416 available bytes; 97.60% used; 225822234 free inodes.

server3 `/tmp`: 85899841536 available bytes; 95.21% used; 114199589 free inodes.

server3 `/var/tmp`: 85899841536 available bytes; 95.21% used; 114199589 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105768488960 available bytes; 94.10% used; 114349097 free inodes.

server4 `/home`: 105768488960 available bytes; 94.10% used; 114349097 free inodes.

server4 `/data`: 254549852160 available bytes; 96.48% used; 225273458 free inodes.

server4 `/tmp`: 105768488960 available bytes; 94.10% used; 114349097 free inodes.

server4 `/var/tmp`: 105768488960 available bytes; 94.10% used; 114349097 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.

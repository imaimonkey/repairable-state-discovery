# V2R cluster inventory

2026-09-24T09:43:07.156495+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324452655104 available bytes; 81.90% used; 112489727 free inodes.

server1 `/home`: 324452655104 available bytes; 81.90% used; 112489727 free inodes.

server1 `/tmp`: 324452655104 available bytes; 81.90% used; 112489727 free inodes.

server1 `/var/tmp`: 324452655104 available bytes; 81.90% used; 112489727 free inodes.

server1 `/mnt/raid5`: 501801340928 available bytes; 97.70% used; 337711804 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57764257792 available bytes; 96.78% used; 110430786 free inodes.

server2 `/home`: 57764257792 available bytes; 96.78% used; 110430786 free inodes.

server2 `/tmp`: 57764257792 available bytes; 96.78% used; 110430786 free inodes.

server2 `/var/tmp`: 57764257792 available bytes; 96.78% used; 110430786 free inodes.

server2 `/mnt/raid5`: 514199220224 available bytes; 96.45% used; 445177125 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85833641984 available bytes; 95.21% used; 114199440 free inodes.

server3 `/home`: 85833641984 available bytes; 95.21% used; 114199440 free inodes.

server3 `/data`: 165693059072 available bytes; 97.71% used; 225819949 free inodes.

server3 `/tmp`: 85833641984 available bytes; 95.21% used; 114199440 free inodes.

server3 `/var/tmp`: 85833641984 available bytes; 95.21% used; 114199440 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105748692992 available bytes; 94.10% used; 114349034 free inodes.

server4 `/home`: 105748692992 available bytes; 94.10% used; 114349034 free inodes.

server4 `/data`: 154557595648 available bytes; 97.86% used; 225273206 free inodes.

server4 `/tmp`: 105748692992 available bytes; 94.10% used; 114349034 free inodes.

server4 `/var/tmp`: 105748692992 available bytes; 94.10% used; 114349034 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.

# V2R cluster inventory

2026-09-23T16:23:11.952457+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | False | [] | [] | reference_compatible=False |
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 41409773568 available bytes; 97.69% used; 110435185 free inodes.

server2 `/home`: 41409773568 available bytes; 97.69% used; 110435185 free inodes.

server2 `/tmp`: 41409773568 available bytes; 97.69% used; 110435185 free inodes.

server2 `/var/tmp`: 41409773568 available bytes; 97.69% used; 110435185 free inodes.

server2 `/mnt/raid5`: 549026164736 available bytes; 96.21% used; 445217976 free inodes.
| server3 | True | ['0'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 284649975808 available bytes; 84.12% used; 114295682 free inodes.

server3 `/home`: 284649975808 available bytes; 84.12% used; 114295682 free inodes.

server3 `/data`: 114161975296 available bytes; 98.42% used; 225854258 free inodes.

server3 `/tmp`: 284649975808 available bytes; 84.12% used; 114295682 free inodes.

server3 `/var/tmp`: 284649975808 available bytes; 84.12% used; 114295682 free inodes.
| server4 | True | ['1', '2', '3', '5', '6'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111498739712 available bytes; 93.78% used; 114375794 free inodes.

server4 `/home`: 111498739712 available bytes; 93.78% used; 114375794 free inodes.

server4 `/data`: 37333131264 available bytes; 99.48% used; 225486421 free inodes.

server4 `/tmp`: 111498739712 available bytes; 93.78% used; 114375794 free inodes.

server4 `/var/tmp`: 111498739712 available bytes; 93.78% used; 114375794 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.

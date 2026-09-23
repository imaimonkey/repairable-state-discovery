# V2R cluster inventory

2026-09-23T16:41:31.986909+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | False | [] | [] | reference_compatible=False |
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 41401896960 available bytes; 97.69% used; 110435443 free inodes.

server2 `/home`: 41401896960 available bytes; 97.69% used; 110435443 free inodes.

server2 `/tmp`: 41401896960 available bytes; 97.69% used; 110435443 free inodes.

server2 `/var/tmp`: 41401896960 available bytes; 97.69% used; 110435443 free inodes.

server2 `/mnt/raid5`: 548470116352 available bytes; 96.21% used; 445217286 free inodes.
| server3 | True | ['0'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 299611324416 available bytes; 83.28% used; 114276227 free inodes.

server3 `/home`: 299611324416 available bytes; 83.28% used; 114276227 free inodes.

server3 `/data`: 95351234560 available bytes; 98.68% used; 225853603 free inodes.

server3 `/tmp`: 299611324416 available bytes; 83.28% used; 114276227 free inodes.

server3 `/var/tmp`: 299611324416 available bytes; 83.28% used; 114276227 free inodes.
| server4 | True | ['1', '2', '3', '5', '6'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111498371072 available bytes; 93.78% used; 114375794 free inodes.

server4 `/home`: 111498371072 available bytes; 93.78% used; 114375794 free inodes.

server4 `/data`: 36169129984 available bytes; 99.50% used; 225477983 free inodes.

server4 `/tmp`: 111498371072 available bytes; 93.78% used; 114375794 free inodes.

server4 `/var/tmp`: 111498371072 available bytes; 93.78% used; 114375794 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.

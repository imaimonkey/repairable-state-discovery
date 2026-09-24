# V2R cluster inventory

2026-09-24T05:34:13.495130+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324537139200 available bytes; 81.90% used; 112492320 free inodes.

server1 `/home`: 324537139200 available bytes; 81.90% used; 112492320 free inodes.

server1 `/tmp`: 324537139200 available bytes; 81.90% used; 112492320 free inodes.

server1 `/var/tmp`: 324537139200 available bytes; 81.90% used; 112492320 free inodes.

server1 `/mnt/raid5`: 517643542528 available bytes; 97.63% used; 337724005 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57916325888 available bytes; 96.77% used; 110431358 free inodes.

server2 `/home`: 57916325888 available bytes; 96.77% used; 110431358 free inodes.

server2 `/tmp`: 57916325888 available bytes; 96.77% used; 110431358 free inodes.

server2 `/var/tmp`: 57916325888 available bytes; 96.77% used; 110431358 free inodes.

server2 `/mnt/raid5`: 522256732160 available bytes; 96.39% used; 445194031 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 127207026688 available bytes; 92.90% used; 114199015 free inodes.

server3 `/home`: 127207026688 available bytes; 92.90% used; 114199015 free inodes.

server3 `/data`: 185265098752 available bytes; 97.44% used; 225839310 free inodes.

server3 `/tmp`: 127207026688 available bytes; 92.90% used; 114199015 free inodes.

server3 `/var/tmp`: 127207026688 available bytes; 92.90% used; 114199015 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105816846336 available bytes; 94.10% used; 114349365 free inodes.

server4 `/home`: 105816846336 available bytes; 94.10% used; 114349365 free inodes.

server4 `/data`: 251510829056 available bytes; 96.52% used; 225358072 free inodes.

server4 `/tmp`: 105816846336 available bytes; 94.10% used; 114349365 free inodes.

server4 `/var/tmp`: 105816846336 available bytes; 94.10% used; 114349365 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.

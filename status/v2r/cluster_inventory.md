# V2R cluster inventory

2026-09-24T05:29:30.001909+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324551815168 available bytes; 81.89% used; 112492369 free inodes.

server1 `/home`: 324551815168 available bytes; 81.89% used; 112492369 free inodes.

server1 `/tmp`: 324551815168 available bytes; 81.89% used; 112492369 free inodes.

server1 `/var/tmp`: 324551815168 available bytes; 81.89% used; 112492369 free inodes.

server1 `/mnt/raid5`: 516193394688 available bytes; 97.63% used; 337724250 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57163759616 available bytes; 96.81% used; 110431193 free inodes.

server2 `/home`: 57163759616 available bytes; 96.81% used; 110431193 free inodes.

server2 `/tmp`: 57163759616 available bytes; 96.81% used; 110431193 free inodes.

server2 `/var/tmp`: 57163759616 available bytes; 96.81% used; 110431193 free inodes.

server2 `/mnt/raid5`: 522405060608 available bytes; 96.39% used; 445193750 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 168503963648 available bytes; 90.60% used; 114198870 free inodes.

server3 `/home`: 168503963648 available bytes; 90.60% used; 114198870 free inodes.

server3 `/data`: 124376915968 available bytes; 98.28% used; 225839629 free inodes.

server3 `/tmp`: 168503963648 available bytes; 90.60% used; 114198870 free inodes.

server3 `/var/tmp`: 168503963648 available bytes; 90.60% used; 114198870 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105817055232 available bytes; 94.10% used; 114349363 free inodes.

server4 `/home`: 105817055232 available bytes; 94.10% used; 114349363 free inodes.

server4 `/data`: 251530534912 available bytes; 96.52% used; 225358119 free inodes.

server4 `/tmp`: 105817055232 available bytes; 94.10% used; 114349363 free inodes.

server4 `/var/tmp`: 105817055232 available bytes; 94.10% used; 114349363 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.

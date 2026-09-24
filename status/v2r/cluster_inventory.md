# V2R cluster inventory

2026-09-24T02:59:30.525269+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325375647744 available bytes; 81.85% used; 112498535 free inodes.

server1 `/home`: 325375647744 available bytes; 81.85% used; 112498535 free inodes.

server1 `/tmp`: 325375647744 available bytes; 81.85% used; 112498535 free inodes.

server1 `/var/tmp`: 325375647744 available bytes; 81.85% used; 112498535 free inodes.

server1 `/mnt/raid5`: 522057478144 available bytes; 97.61% used; 337732350 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40863416320 available bytes; 97.72% used; 110431330 free inodes.

server2 `/home`: 40863416320 available bytes; 97.72% used; 110431330 free inodes.

server2 `/tmp`: 40863416320 available bytes; 97.72% used; 110431330 free inodes.

server2 `/var/tmp`: 40863416320 available bytes; 97.72% used; 110431330 free inodes.

server2 `/mnt/raid5`: 528105541632 available bytes; 96.35% used; 445198597 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292287086592 available bytes; 83.69% used; 114186960 free inodes.

server3 `/home`: 292287086592 available bytes; 83.69% used; 114186960 free inodes.

server3 `/data`: 39710785536 available bytes; 99.45% used; 225845359 free inodes.

server3 `/tmp`: 292287086592 available bytes; 83.69% used; 114186960 free inodes.

server3 `/var/tmp`: 292287086592 available bytes; 83.69% used; 114186960 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105996828672 available bytes; 94.08% used; 114349629 free inodes.

server4 `/home`: 105996828672 available bytes; 94.08% used; 114349629 free inodes.

server4 `/data`: 289712701440 available bytes; 96.00% used; 225386863 free inodes.

server4 `/tmp`: 105996828672 available bytes; 94.08% used; 114349629 free inodes.

server4 `/var/tmp`: 105996828672 available bytes; 94.08% used; 114349629 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.

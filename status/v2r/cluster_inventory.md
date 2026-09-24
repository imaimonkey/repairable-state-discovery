# V2R cluster inventory

2026-09-24T03:02:37.686607+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325372116992 available bytes; 81.85% used; 112498510 free inodes.

server1 `/home`: 325372116992 available bytes; 81.85% used; 112498510 free inodes.

server1 `/tmp`: 325372116992 available bytes; 81.85% used; 112498510 free inodes.

server1 `/var/tmp`: 325372116992 available bytes; 81.85% used; 112498510 free inodes.

server1 `/mnt/raid5`: 508726546432 available bytes; 97.67% used; 337732245 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40861081600 available bytes; 97.72% used; 110431302 free inodes.

server2 `/home`: 40861081600 available bytes; 97.72% used; 110431302 free inodes.

server2 `/tmp`: 40861081600 available bytes; 97.72% used; 110431302 free inodes.

server2 `/var/tmp`: 40861081600 available bytes; 97.72% used; 110431302 free inodes.

server2 `/mnt/raid5`: 527994548224 available bytes; 96.35% used; 445198517 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292289355776 available bytes; 83.69% used; 114187109 free inodes.

server3 `/home`: 292289355776 available bytes; 83.69% used; 114187109 free inodes.

server3 `/data`: 39700242432 available bytes; 99.45% used; 225845302 free inodes.

server3 `/tmp`: 292289355776 available bytes; 83.69% used; 114187109 free inodes.

server3 `/var/tmp`: 292289355776 available bytes; 83.69% used; 114187109 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105988333568 available bytes; 94.09% used; 114349629 free inodes.

server4 `/home`: 105988333568 available bytes; 94.09% used; 114349629 free inodes.

server4 `/data`: 289712812032 available bytes; 96.00% used; 225386865 free inodes.

server4 `/tmp`: 105988333568 available bytes; 94.09% used; 114349629 free inodes.

server4 `/var/tmp`: 105988333568 available bytes; 94.09% used; 114349629 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.

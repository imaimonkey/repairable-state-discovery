# V2R cluster inventory

2026-09-24T02:23:38.172137+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325392105472 available bytes; 81.85% used; 112498949 free inodes.

server1 `/home`: 325392105472 available bytes; 81.85% used; 112498949 free inodes.

server1 `/tmp`: 325392105472 available bytes; 81.85% used; 112498949 free inodes.

server1 `/var/tmp`: 325392105472 available bytes; 81.85% used; 112498949 free inodes.

server1 `/mnt/raid5`: 675005448192 available bytes; 96.90% used; 337733244 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40892854272 available bytes; 97.72% used; 110431584 free inodes.

server2 `/home`: 40892854272 available bytes; 97.72% used; 110431584 free inodes.

server2 `/tmp`: 40892854272 available bytes; 97.72% used; 110431584 free inodes.

server2 `/var/tmp`: 40892854272 available bytes; 97.72% used; 110431584 free inodes.

server2 `/mnt/raid5`: 529231486976 available bytes; 96.34% used; 445199964 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 291858366464 available bytes; 83.71% used; 114163143 free inodes.

server3 `/home`: 291858366464 available bytes; 83.71% used; 114163143 free inodes.

server3 `/data`: 39766142976 available bytes; 99.45% used; 225846901 free inodes.

server3 `/tmp`: 291858366464 available bytes; 83.71% used; 114163143 free inodes.

server3 `/var/tmp`: 291858366464 available bytes; 83.71% used; 114163143 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106012430336 available bytes; 94.08% used; 114349853 free inodes.

server4 `/home`: 106012430336 available bytes; 94.08% used; 114349853 free inodes.

server4 `/data`: 289739476992 available bytes; 96.00% used; 225387624 free inodes.

server4 `/tmp`: 106012430336 available bytes; 94.08% used; 114349853 free inodes.

server4 `/var/tmp`: 106012430336 available bytes; 94.08% used; 114349853 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.

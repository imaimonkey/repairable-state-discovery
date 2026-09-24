# V2R cluster inventory

2026-09-24T06:41:19.209985+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324499619840 available bytes; 81.90% used; 112491564 free inodes.

server1 `/home`: 324499619840 available bytes; 81.90% used; 112491564 free inodes.

server1 `/tmp`: 324499619840 available bytes; 81.90% used; 112491564 free inodes.

server1 `/var/tmp`: 324499619840 available bytes; 81.90% used; 112491564 free inodes.

server1 `/mnt/raid5`: 517569355776 available bytes; 97.63% used; 337723748 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57873469440 available bytes; 96.77% used; 110431191 free inodes.

server2 `/home`: 57873469440 available bytes; 96.77% used; 110431191 free inodes.

server2 `/tmp`: 57873469440 available bytes; 96.77% used; 110431191 free inodes.

server2 `/var/tmp`: 57873469440 available bytes; 96.77% used; 110431191 free inodes.

server2 `/mnt/raid5`: 519903879168 available bytes; 96.41% used; 445191819 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 127011069952 available bytes; 92.91% used; 114196353 free inodes.

server3 `/home`: 127011069952 available bytes; 92.91% used; 114196353 free inodes.

server3 `/data`: 139385344000 available bytes; 98.07% used; 225835507 free inodes.

server3 `/tmp`: 127011069952 available bytes; 92.91% used; 114196353 free inodes.

server3 `/var/tmp`: 127011069952 available bytes; 92.91% used; 114196353 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105804775424 available bytes; 94.10% used; 114349244 free inodes.

server4 `/home`: 105804775424 available bytes; 94.10% used; 114349244 free inodes.

server4 `/data`: 318334992384 available bytes; 95.60% used; 225372269 free inodes.

server4 `/tmp`: 105804775424 available bytes; 94.10% used; 114349244 free inodes.

server4 `/var/tmp`: 105804775424 available bytes; 94.10% used; 114349244 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.

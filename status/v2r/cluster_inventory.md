# V2R cluster inventory

2026-09-24T09:29:09.432440+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324459511808 available bytes; 81.90% used; 112489870 free inodes.

server1 `/home`: 324459511808 available bytes; 81.90% used; 112489870 free inodes.

server1 `/tmp`: 324459511808 available bytes; 81.90% used; 112489870 free inodes.

server1 `/var/tmp`: 324459511808 available bytes; 81.90% used; 112489870 free inodes.

server1 `/mnt/raid5`: 502504300544 available bytes; 97.69% used; 337713481 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57769762816 available bytes; 96.78% used; 110430811 free inodes.

server2 `/home`: 57769762816 available bytes; 96.78% used; 110430811 free inodes.

server2 `/tmp`: 57769762816 available bytes; 96.78% used; 110430811 free inodes.

server2 `/var/tmp`: 57769762816 available bytes; 96.78% used; 110430811 free inodes.

server2 `/mnt/raid5`: 514095857664 available bytes; 96.45% used; 445177682 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85438337024 available bytes; 95.23% used; 114174511 free inodes.

server3 `/home`: 85438337024 available bytes; 95.23% used; 114174511 free inodes.

server3 `/data`: 165811404800 available bytes; 97.71% used; 225820898 free inodes.

server3 `/tmp`: 85438337024 available bytes; 95.23% used; 114174511 free inodes.

server3 `/var/tmp`: 85438337024 available bytes; 95.23% used; 114174511 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105757777920 available bytes; 94.10% used; 114349047 free inodes.

server4 `/home`: 105757777920 available bytes; 94.10% used; 114349047 free inodes.

server4 `/data`: 154938953728 available bytes; 97.86% used; 225273297 free inodes.

server4 `/tmp`: 105757777920 available bytes; 94.10% used; 114349047 free inodes.

server4 `/var/tmp`: 105757777920 available bytes; 94.10% used; 114349047 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.

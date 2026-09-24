# V2R cluster inventory

2026-09-24T06:33:32.874655+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324504997888 available bytes; 81.90% used; 112491633 free inodes.

server1 `/home`: 324504997888 available bytes; 81.90% used; 112491633 free inodes.

server1 `/tmp`: 324504997888 available bytes; 81.90% used; 112491633 free inodes.

server1 `/var/tmp`: 324504997888 available bytes; 81.90% used; 112491633 free inodes.

server1 `/mnt/raid5`: 517579116544 available bytes; 97.63% used; 337723760 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57881751552 available bytes; 96.77% used; 110431211 free inodes.

server2 `/home`: 57881751552 available bytes; 96.77% used; 110431211 free inodes.

server2 `/tmp`: 57881751552 available bytes; 96.77% used; 110431211 free inodes.

server2 `/var/tmp`: 57881751552 available bytes; 96.77% used; 110431211 free inodes.

server2 `/mnt/raid5`: 520128176128 available bytes; 96.41% used; 445191792 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 127198199808 available bytes; 92.90% used; 114197414 free inodes.

server3 `/home`: 127198199808 available bytes; 92.90% used; 114197414 free inodes.

server3 `/data`: 139443490816 available bytes; 98.07% used; 225835684 free inodes.

server3 `/tmp`: 127198199808 available bytes; 92.90% used; 114197414 free inodes.

server3 `/var/tmp`: 127198199808 available bytes; 92.90% used; 114197414 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105805320192 available bytes; 94.10% used; 114349268 free inodes.

server4 `/home`: 105805320192 available bytes; 94.10% used; 114349268 free inodes.

server4 `/data`: 325950304256 available bytes; 95.50% used; 225372816 free inodes.

server4 `/tmp`: 105805320192 available bytes; 94.10% used; 114349268 free inodes.

server4 `/var/tmp`: 105805320192 available bytes; 94.10% used; 114349268 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.

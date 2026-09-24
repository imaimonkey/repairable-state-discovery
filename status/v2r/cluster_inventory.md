# V2R cluster inventory

2026-09-24T09:51:00.509761+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324445261824 available bytes; 81.90% used; 112489622 free inodes.

server1 `/home`: 324445261824 available bytes; 81.90% used; 112489622 free inodes.

server1 `/tmp`: 324445261824 available bytes; 81.90% used; 112489622 free inodes.

server1 `/var/tmp`: 324445261824 available bytes; 81.90% used; 112489622 free inodes.

server1 `/mnt/raid5`: 500740182016 available bytes; 97.70% used; 337702484 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57756381184 available bytes; 96.78% used; 110430765 free inodes.

server2 `/home`: 57756381184 available bytes; 96.78% used; 110430765 free inodes.

server2 `/tmp`: 57756381184 available bytes; 96.78% used; 110430765 free inodes.

server2 `/var/tmp`: 57756381184 available bytes; 96.78% used; 110430765 free inodes.

server2 `/mnt/raid5`: 513974808576 available bytes; 96.45% used; 445177295 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85829169152 available bytes; 95.21% used; 114199355 free inodes.

server3 `/home`: 85829169152 available bytes; 95.21% used; 114199355 free inodes.

server3 `/data`: 165630537728 available bytes; 97.71% used; 225819786 free inodes.

server3 `/tmp`: 85829169152 available bytes; 95.21% used; 114199355 free inodes.

server3 `/var/tmp`: 85829169152 available bytes; 95.21% used; 114199355 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105748385792 available bytes; 94.10% used; 114349031 free inodes.

server4 `/home`: 105748385792 available bytes; 94.10% used; 114349031 free inodes.

server4 `/data`: 154553589760 available bytes; 97.86% used; 225273209 free inodes.

server4 `/tmp`: 105748385792 available bytes; 94.10% used; 114349031 free inodes.

server4 `/var/tmp`: 105748385792 available bytes; 94.10% used; 114349031 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.

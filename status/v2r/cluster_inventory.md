# V2R cluster inventory

2026-09-24T10:59:19.966059+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324377735168 available bytes; 81.90% used; 112489046 free inodes.

server1 `/home`: 324377735168 available bytes; 81.90% used; 112489046 free inodes.

server1 `/tmp`: 324377735168 available bytes; 81.90% used; 112489046 free inodes.

server1 `/var/tmp`: 324377735168 available bytes; 81.90% used; 112489046 free inodes.

server1 `/mnt/raid5`: 491574755328 available bytes; 97.74% used; 337693591 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 57698865152 available bytes; 96.78% used; 110430303 free inodes.

server2 `/home`: 57698865152 available bytes; 96.78% used; 110430303 free inodes.

server2 `/tmp`: 57698865152 available bytes; 96.78% used; 110430303 free inodes.

server2 `/var/tmp`: 57698865152 available bytes; 96.78% used; 110430303 free inodes.

server2 `/mnt/raid5`: 511365259264 available bytes; 96.47% used; 445174538 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85771644928 available bytes; 95.21% used; 114196657 free inodes.

server3 `/home`: 85771644928 available bytes; 95.21% used; 114196657 free inodes.

server3 `/data`: 164025008128 available bytes; 97.73% used; 225817620 free inodes.

server3 `/tmp`: 85771644928 available bytes; 95.21% used; 114196657 free inodes.

server3 `/var/tmp`: 85771644928 available bytes; 95.21% used; 114196657 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105734742016 available bytes; 94.10% used; 114348930 free inodes.

server4 `/home`: 105734742016 available bytes; 94.10% used; 114348930 free inodes.

server4 `/data`: 132773203968 available bytes; 98.17% used; 225258252 free inodes.

server4 `/tmp`: 105734742016 available bytes; 94.10% used; 114348930 free inodes.

server4 `/var/tmp`: 105734742016 available bytes; 94.10% used; 114348930 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.

# V2R cluster inventory

2026-09-24T10:28:17.482420+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324411486208 available bytes; 81.90% used; 112489278 free inodes.

server1 `/home`: 324411486208 available bytes; 81.90% used; 112489278 free inodes.

server1 `/tmp`: 324411486208 available bytes; 81.90% used; 112489278 free inodes.

server1 `/var/tmp`: 324411486208 available bytes; 81.90% used; 112489278 free inodes.

server1 `/mnt/raid5`: 500167512064 available bytes; 97.71% used; 337698046 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57735475200 available bytes; 96.78% used; 110430675 free inodes.

server2 `/home`: 57735475200 available bytes; 96.78% used; 110430675 free inodes.

server2 `/tmp`: 57735475200 available bytes; 96.78% used; 110430675 free inodes.

server2 `/var/tmp`: 57735475200 available bytes; 96.78% used; 110430675 free inodes.

server2 `/mnt/raid5`: 512785534976 available bytes; 96.46% used; 445175417 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85366263808 available bytes; 95.24% used; 114173297 free inodes.

server3 `/home`: 85366263808 available bytes; 95.24% used; 114173297 free inodes.

server3 `/data`: 164322377728 available bytes; 97.73% used; 225818669 free inodes.

server3 `/tmp`: 85366263808 available bytes; 95.24% used; 114173297 free inodes.

server3 `/var/tmp`: 85366263808 available bytes; 95.24% used; 114173297 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105744629760 available bytes; 94.10% used; 114348968 free inodes.

server4 `/home`: 105744629760 available bytes; 94.10% used; 114348968 free inodes.

server4 `/data`: 153472860160 available bytes; 97.88% used; 225258405 free inodes.

server4 `/tmp`: 105744629760 available bytes; 94.10% used; 114348968 free inodes.

server4 `/var/tmp`: 105744629760 available bytes; 94.10% used; 114348968 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.

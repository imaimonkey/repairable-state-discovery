# V2R cluster inventory

2026-09-24T10:25:11.349504+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324413964288 available bytes; 81.90% used; 112489308 free inodes.

server1 `/home`: 324413964288 available bytes; 81.90% used; 112489308 free inodes.

server1 `/tmp`: 324413964288 available bytes; 81.90% used; 112489308 free inodes.

server1 `/var/tmp`: 324413964288 available bytes; 81.90% used; 112489308 free inodes.

server1 `/mnt/raid5`: 500172500992 available bytes; 97.71% used; 337698403 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57735806976 available bytes; 96.78% used; 110430677 free inodes.

server2 `/home`: 57735806976 available bytes; 96.78% used; 110430677 free inodes.

server2 `/tmp`: 57735806976 available bytes; 96.78% used; 110430677 free inodes.

server2 `/var/tmp`: 57735806976 available bytes; 96.78% used; 110430677 free inodes.

server2 `/mnt/raid5`: 512881704960 available bytes; 96.46% used; 445175706 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85806080000 available bytes; 95.21% used; 114198535 free inodes.

server3 `/home`: 85806080000 available bytes; 95.21% used; 114198535 free inodes.

server3 `/data`: 164342673408 available bytes; 97.73% used; 225818718 free inodes.

server3 `/tmp`: 85806080000 available bytes; 95.21% used; 114198535 free inodes.

server3 `/var/tmp`: 85806080000 available bytes; 95.21% used; 114198535 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105744887808 available bytes; 94.10% used; 114348981 free inodes.

server4 `/home`: 105744887808 available bytes; 94.10% used; 114348981 free inodes.

server4 `/data`: 153472294912 available bytes; 97.88% used; 225258401 free inodes.

server4 `/tmp`: 105744887808 available bytes; 94.10% used; 114348981 free inodes.

server4 `/var/tmp`: 105744887808 available bytes; 94.10% used; 114348981 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
